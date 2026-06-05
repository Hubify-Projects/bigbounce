# P1A R10v3 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: 244.7s

---

# Referee Report: P1A — "Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter"

**Submission:** Physical Review D
**Reviewer stance:** Brutal honesty

---

## Overall Assessment

This paper attempts to do something unusual: claim a *negative* structural result (closing four channels by which Einstein-Cartan-Holst gravity could source dark energy), accompanied by a perturbation-transparency theorem, while simultaneously hedging that none of this actually constitutes an operator-level no-go. The result is a manuscript that reads as if it is constantly negotiating with itself. The abstract alone contains five distinct hedge clauses qualifying the central claim. The body extends and re-qualifies these hedges across 21 pages. The actual *new* physics content — that the Holst term on a torsion-free connection reduces to the Pontryagin density and is thus a boundary term — is essentially a one-paragraph observation already implicit in Hehl et al. (1976) and Mercuri (2009). Nearly everything else is bookkeeping that the author admits is a "phenomenological ansatz, not a derivation."

The paper is too long for its actual contribution by at least a factor of three, the abstract overclaims, the central "13 logically-independent constraints / 14 historical entries" structure is internally inconsistent (more on this below), the dimensional analysis in Appendix B is candidly broken (the author admits this in the text), and the manuscript is riddled with companion-paper references to works "in preparation," several of which carry load-bearing numbers (σ(fNL), ∆Neff posteriors, H₀, MCMC convergence) that the present paper cites as established.

---

## ESSENTIAL findings (must fix before acceptance)

### P1A-E1: Self-undermining central claim
**Location:** Abstract, p. 1; Sec. I "Scope and limitations," p. 3; Sec. IV "Scope," p. 8; Sec. XI; Appendix B.
**Problem:** The abstract states the four routes are *closed* at amplitude level, then immediately states "the four enumerated routes ... are *not proven to be a complete* diffeomorphism-invariant operator basis," that "missing operators" exist (Jackiw–Pi gravitational Chern–Simons and a parity-odd four-fermion partner), and that "the dark-energy mapping rests on a phenomenological on-shell scaling ansatz whose off-shell mass dimension is +1 rather than +4." In Appendix B the author writes outright: "We acknowledge openly that this operator, as written, is not a controlled dimension-+4 EFT operator." A "channel-level closure" whose own enumeration is admittedly incomplete *and* whose dimensional analysis is admittedly broken is not a closure result publishable in PRD. The title and abstract overclaim. Either (a) close the operator basis (i.e. do the work the author defers to "follow-up") or (b) rewrite as a perturbation-transparency note plus a discussion of phenomenological obstructions.
**Required fix:** Restructure as a focused paper on the perturbation-transparency observation (Sec. X), with the four-route material as discussion. Drop "channel-level closure" framing from title and abstract. Remove the explicit list of missing operators from the abstract — putting one's own scope-violations in the abstract does not absolve them.

### P1A-E2: Appendix B admits the dark-energy mapping is dimensionally inconsistent
**Location:** Appendix B, p. 19.
**Problem:** Eq. (B1) gives the parity-odd operator off-shell mass dimension +1 (three units short of the required +4). The author then writes that "Inserting on-shell background curvature factors or a phenomenological 'volume-integration-density' factor of M²_Pl does *not* constitute a derivation; the missing powers of mass do not arise from off-shell EFT counting but from on-shell scaling assumptions." This is a fatal admission for the entire ρ_Λ derivation in Sec. II C (Eq. 10) and the Sec. XII A bookkeeping. The 10⁻¹²³ "result" rests on three missing mass dimensions assigned by ansatz. This is not adequate for PRD. The Ξ ≈ 10⁻¹²³ matching, the Ntot ≈ 92 e-fold number, and the "fine-tuning reduction from 10¹²² to 10⁵" all inherit this defect.
**Required fix:** Either supply a controlled dimension-+4 operator with explicit coupling (M³_Pl factors in the coefficient justified, not asserted), or explicitly state in the abstract that ρ_Λ ∼ Ξ M⁴_Pl is *not derived* and remove the e-fold matching as a quantitative result.

### P1A-E3: 13 vs 14 barriers — internally inconsistent counting throughout
**Location:** Abstract (p. 1, "13 logically-independent ... 14 historical catalog entries, of which B8 is subsumed by B14"); Sec. IX (p. 12, lists 14); Table II (p. 13, lists 14); Sec. XV (p. 18, "14 mechanism-class constraints" then "13 logically-independent barriers"); Sec. XIV E.
**Problem:** The paper oscillates between "13" and "14" constraints throughout, with a footnote-style explanation that B8 is "the observational consequence of B14" and "retained for historical mechanism-class completeness." This is internal-audit residue. If B8 is not independent of B14, then it is one constraint — drop B8 from Table II and the numbered list, present 13 throughout, and stop using the phrase "historical catalog entry" which is review-log language, not scientific content. Currently the reader has to track two parallel counting systems for the entire paper.
**Required fix:** Eliminate B8 or merge it with B14 explicitly. Present a single consistent count.

### P1A-E4: Companion-paper dependence for load-bearing numbers
**Location:** Throughout — Table I (H₀, ∆Neff), p. 8 ("MCMC verification"), Sec. VII (σ(fNL) ≈ 0.7), Table IV (cosmological parameters), Sec. XIII, etc.
**Problem:** The paper repeatedly cites companion Paper I(b) [6], Paper II [2], Paper III [46], Paper IV [23] — *all "in preparation"* — for results that load-bear in this paper. H₀ = 67.68 ± 1.06, ∆Neff = −0.020 ± 0.169, σ(fNL) = 0.7 forecast, 309,189 frozen MCMC samples, γ_PTA = 2.567 ± 0.382 from "real-KDE GPU MCMC," NaMaster pipeline validation, ALP MCMC with 9,720 samples and R̂ − 1 < 0.01 — none of these are verifiable. The author acknowledges this on p. 5: "they are documented internally rather than as externally citable arXiv-posted numbers, and should be read as internal-analysis inputs to the present structural argument rather than as independently peer-reviewable values until Paper I(b) is publicly posted." That is precisely the problem: PRD does not accept submissions whose load-bearing numbers are not independently verifiable.
**Required fix:** Either (a) post the companion papers to arXiv simultaneously and supply DOIs, or (b) remove every quantitative claim that depends on them and rewrite as a purely theoretical paper.

### P1A-E5: AI assistance disclosure is inadequate
**Location:** Acknowledgments, p. 18.
**Problem:** The author writes "The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic barrier-cataloging, perturbation-gate verification, and manuscript preparation. All scientific claims, derivations, numerical results, and bibliographic attributions were independently verified by the author." Given that "barrier cataloging" and "perturbation-gate verification" are *the central contributions* of the paper, having an AI do this is not a minor methodological note. APS policy requires explicit disclosure of AI use scope. The current language is too vague: was the 14-barrier list AI-generated and human-checked, AI-extended from a human-drafted core, or human-authored with AI editorial assistance? This matters for assessing originality.
**Required fix:** Specify precisely what AI did. If AI generated the barrier taxonomy or the perturbation-transparency observation, disclose. If AI was only a writing tool, narrow the language.

### P1A-E6: SPHEREx fNL significance — undisclosed double-citation of a forecast
**Location:** Sec. VII footnote 1 (p. 11), Sec. XIII, Sec. I Table I, Sec. III B.
**Problem:** The 3–5σ realistic significance for SPHEREx fNL is cited repeatedly as a load-bearing prediction. The footnote explains the "Fisher-ideal" σ(fNL) ≈ 0.7 and the "post-systematic" σ(fNL) ≈ 1.0. But fNL = −35/8 = −4.375, and |fNL|/σ = 4.375/0.7 = 6.25σ (Fisher-ideal) and 4.375/1.0 = 4.375σ (with systematics) — i.e. the *lower* bound at 4.375σ already exceeds the "3σ" lower endpoint claimed. The author then mentions a "template-overlap correction r ≈ 0.84" that degrades to "5–5.5σ optimistic." Where does the "3σ" come from? It appears nowhere in the arithmetic. Either the Heinrich et al. 2024 number is being misused or the GR-projection and bϕ degradation factors are doing unstated work that is not in the footnote. As written, the range "3–5σ" is not derivable from the numbers given.
**Required fix:** Show the arithmetic: r, GR-projection factor, bϕ uncertainty, photo-z. Or remove the "3σ" lower bound.

### P1A-E7: Eq. (15) dimensional gymnastics
**Location:** Sec. IV B, p. 9.
**Problem:** The author explicitly writes "(A naive comparison of a rotation rate β̇ in eV against an angle uncertainty in eV would silently treat eV·s as dimensionless; the dimensionless reduction above avoids this and recovers the standard R2 amplitude-suppression closure.)" — flagging in the text that an earlier derivation had a dimensional error. Then Eq. (15) presents two contractions that yield 10⁻⁵⁸ vs 10⁻³³ (a 25-orders-of-magnitude spread depending on "ordering"). The author resolves this with "We adopt this contraction as the canonical Route-2 estimate." This is not how amplitude no-go arguments work: if two equivalent orderings of the same dimensionless ratio differ by 10²⁵, the calculation is wrong, not "ordering-dependent." A dimensionless ratio has one value.
**Required fix:** Redo the calculation cleanly. State the operator, the matrix element, the integration measure. Get one number, not two.

### P1A-E8: Route 4 closure inverted mid-paper
**Location:** Sec. IV D (p. 10), Sec. IV E (p. 11), Sec. II C (p. 6).
**Problem:** Section II C and the abstract describe Route 4 as if it provides the surviving birefringence prediction. Section IV D then states Route 4 is closed by "a naturalness objection rather than an amplitude exclusion," with the explicit text: "R4 is therefore *not* closed by amplitude mismatch (as prior analyses claimed); it is closed by the observation that the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H₀ to also produce ρ_Λ." This is a major shift from amplitude no-go to "naturalness objection," and the abstract does not reflect it. Worse, this means Route 4 *does* match β_obs with the fitted coupling — i.e. the headline "all four routes close" is misleading. R4 is left as an "explanatory deficit," which is not a closure.
**Required fix:** Either accept Route 4 closure is naturalness-only and reword abstract and title accordingly, or provide an amplitude-level closure. The current both-and framing is dishonest.

### P1A-E9: Abstract — "two surviving predictions" framing is contradictory
**Location:** Abstract, pp. 1–2.
**Problem:** The abstract first claims "each fails at the amplitude level" and "the minimal-ECH four-route channel set is therefore tightly constrained as both a dark-energy generator and a matter-bounce host," then describes two "surviving" predictions that are "*not* predictions of ECH itself" but bounce-class and GR+ALP-class observables. So: ECH is closed, but the surviving tests are not ECH tests, but they are reported because the closure does not forbid them in complementary parameter regimes. This is incoherent as a structure: the paper claims to close a framework and simultaneously to advertise tests that are not tests of the framework. A reader leaves the abstract with no clear takeaway. This is the abstract for a different paper.
**Required fix:** Rewrite the abstract to either (a) report ECH closure and refer surviving tests to companion papers, or (b) admit the four-route closure is insufficient to constrain the bounce-class framework. Pick one.

### P1A-E10: Structural tension argument is asymmetric and possibly wrong
**Location:** Abstract footnote, Sec. XIV D (p. 17), Sec. XIII.
**Problem:** The author argues that the dark-energy mechanism requires Ntot ≈ 92 e-folds, which erases the fNL = −35/8 prediction at SPHEREx scales. But Ntot ≈ 92 was derived in Appendix B as the e-fold count needed to *match* ρ_Λ from the ansatz Eq. (B2). Then in Sec. XIV D this same number is used to *block* the matter-bounce signal. This is presented as a "structural tension," but Sec. XIV D admits that "the no-go has already closed the four amplitude routes by which minimal ECH could source dark energy, so the structural-tension argument has nothing remaining to bind against at the route-amplitude level." So by the author's own admission this is not a new independent constraint — yet it appears in the abstract as a load-bearing result. Additionally, the e^32 push to subhorizon scales assumes a specific mapping between bounce-epoch comoving wavenumbers and SPHEREx scales that is not derived — the matter-bounce contraction-mode survival depends on the full bounce-to-inflation matching, not just on Ntot.
**Required fix:** Either supply the full matching calculation showing that Ntot > 60 erases the fNL signature (with explicit dependence on the bounce-to-inflation transition), or drop this from the abstract and headline narrative.

### P1A-E11: Eq. (B2) inconsistent with body text
**Location:** Appendix B, p. 19; Sec. II C 1; Sec. XII A.
**Problem:** Eq. (B2) writes ρ_Λ^bounce ∼ (α/M) M⁵_Pl ∼ 10⁻² M⁴_Pl. With α/M ∼ 10⁻²¹ GeV⁻¹ = 10⁻²/M_Pl, this gives (α/M)M⁵_Pl = 10⁻² M⁴_Pl. Fine. But Sec. II C Eq. (10) writes Λ_eff = Ξ M²_Pl with Ξ = [(α/M)M_Pl] D_inf, so Λ_eff has dimensions [M²_Pl] (correct for a cosmological constant entering the Einstein equations). Then the abstract and Sec. XII A treat Ξ as the dimensionless suppression factor relative to M⁴_Pl. These three uses of Ξ are not consistent — sometimes it's dimensionless, sometimes dimensionful, sometimes mapped through Eq. (B2)'s on-shell ansatz. The author acknowledges this in the text but never fixes it.
**Required fix:** Define Ξ once with explicit dimensions, propagate consistently.

### P1A-E12: Internal-audit residue in published text
**Location:** Multiple.
**Problem:** The body contains review-log language that should not appear in a published paper:
 - Sec. X G (p. 15): "This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20±0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6."
 - Sec. XI (p. 15): "the loophole was explored theoretically but the w0wa extension was never implemented computationally in this program"
 - Appendix B (p. 19): "not the ∼ 35 misstated in earlier drafts"; "Either reading is a phenomenological dimensional assignment, not a derivation; we make that status explicit here so the reader is not misled by an apparent 'fix' in earlier drafts."
 - Table III footnote ‡ (p. 16): describes an actively running MCMC chain at "∼3.8×10⁴ accepted samples" with "R̂ − 1 ≈ 3×10⁻²" — a live status report, not a published result.
 - Sec. I Table I (p. 4): footnote a "Reparameterized as sensitivity to Ntot; not solved."
**Required fix:** Strip all version-history and review-process language. A reader should not be told about earlier drafts, superseded values, or actively running chains.

### P1A-E13: Table III row "DESI DR2 w0wa (new)" — live data in a published table
**Location:** Table III footnote ‡, p. 16.
**Problem:** The footnote describes a chain currently running on a "dedicated MPI pod" with current sample count, current R̂, and prose like "we deliberately do not commit to a specific calendar date for convergence in this footnote." This is a project status update, not a publishable footnote. A frozen analysis or no analysis — pick one.
**Required fix:** Remove the live status and either present the converged result or remove the row.

---

## MAJOR findings

### P1A-M1: Eq. (11) "order-of-magnitude matching" is not a derivation
**Location:** Sec. II C 1, pp. 6–7.
**Problem:** The (T_reh/M_GUT)^{3/2} prefactor is justified by the author's own text as "dimensional-analysis aesthetic at this level rather than calculated from a thermal partition function." The half-integer power is said to come from a "parity-odd density-of-states factor that distinguishes the ψ̄γ[aγbγc]ψ axial-vector contraction from the parity-even scalar contraction." This is hand-waving. The whole Ntot ≈ 92 result rests on this prefactor.
**Required fix:** Either derive the prefactor or label Eq. (11) as a parameterization and propagate uncertainty into Ntot.

### P1A-M2: "Reheating thermal-reset barrier" is an *additional* mechanism inserted mid-paper
**Location:** Sec. II C 1, pp. 6–7.
**Problem:** The "reheating thermal-reset barrier (supporting B14)" appears in the middle of the dilution derivation as a separate physical argument. It is then said to "strengthen Barrier 14 (perturbation transparency) by adding a parallel thermodynamic erasure channel." This is a new mechanism, not part of the perturbation-transparency theorem. It deserves its own subsection and clear status. As written it is an inline hedge that admits the e^{−3Ntot} bookkeeping does not actually do the work.
**Required fix:** Either elevate to a separate barrier (B15?) or remove.

### P1A-M3: Fig. 1 — pure schematic with no calculated content
**Location:** Fig. 1, p. 4.
**Problem:** This is a flow diagram showing which bounce mechanisms produce which observables. It contains no numerical content, no equation references, no error budgets — it is essentially a poster slide. PRD figures are expected to carry analyzable content. The figure also implies ECH "produces fNL = −35/8 via matter bounce" with a green arrow while the abstract and Sec. XIII insist this is *not* an ECH prediction. The figure caption and abstract contradict on this point.
**Required fix:** Either replace with a calculated figure (e.g., explicit amplitude ratios for the four routes vs observational bounds) or move to a discussion section.

### P1A-M4: Fig. 2 — energy hierarchy figure asserts the result under critique
**Location:** Fig. 2, p. 5.
**Problem:** Caption explicitly states "This ansatz is dimensionally correct on-shell at the bounce but is not derived from the ECH action." The figure then displays "×e^{−3N} (∼10⁻¹²²)" and "After inflationary dilution" as if it were a derivation, with the units of ρ_vac as M⁴_Pl × 10⁻² (the Eq. B2 ansatz). A figure that displays a result the caption simultaneously disclaims is not a publishable figure.
**Required fix:** Either replace with an honest comparison plot or remove.

### P1A-M5: Table I — claims about H₀ and ∆Neff results cited from companion paper
**Location:** Table I, p. 4.
**Problem:** "H₀ = 67.68 ± 1.06, ∆Neff ≈ 0" cited as if a result of this paper. They are not — they are companion-paper inputs. Footnote a admits "Reparameterized as sensitivity to Ntot; not solved." The table is selling resolution of H₀/σ₈ tension that the paper does not provide.
**Required fix:** Mark all companion-paper-sourced values explicitly. Remove or relabel the "H₀/σ8 tension resolution" row — "Recovers ΛCDM" is not a resolution.

### P1A-M6: Table II — claimed counting is wrong
**Location:** Table II, p. 13.
**Problem:** Table lists 14 entries with the note that B8 is "the observational consequence of the perturbation-transparency theorem B14." If they are not independent, the count is 13, not 14. The table presents both as separate rows. This contradicts the abstract claim of "13 logically-independent" constraints.
**Required fix:** Drop one row or merge.

### P1A-M7: Table IV — γ "uncertainty" labeled as "scheme range"
**Location:** Table IV, p. 20.
**Problem:** The table cell reads "0.274 (scheme range ∼0.020)". The body text (p. 5) explicitly says this is "scheme dependence rather than a statistical or theoretical error." But the table prior column says "Fixed: 0.274" — so what is the 0.020 doing in the value column at all? It is not an uncertainty. It is the spread of competing γ values across U(1)/SU(2)/DLM schemes. Putting it in a value cell next to MCMC posteriors with proper σ misleads.
**Required fix:** Remove the ±0.020 from the γ value cell; explain scheme dependence in a footnote only.

### P1A-M8: Eq. (17) inversion gives wrong scaling consequence
**Location:** Sec. IV D, p. 10.
**Problem:** β = (α/M)√(2ρ_θ/m²_θ) inverts to ρ_θ = m²_θ β²/[2(α/M)²]. With α/M = 10⁻²¹ GeV⁻¹, β ≈ 6×10⁻³ rad, m_θ = H₀ ≈ 1.5×10⁻³³ eV ≈ 1.5×10⁻⁴² GeV: ρ_θ = (1.5×10⁻⁴²)² × (6×10⁻³)² / (2×(10⁻²¹)²) GeV⁴ = (2.25×10⁻⁸⁴) × (3.6×10⁻⁵) / (2×10⁻⁴²) = (8.1×10⁻⁸⁹) / (2×10⁻⁴²) = 4×10⁻⁴⁷ GeV⁴. Converting to eV: 4×10⁻⁴⁷ × (10⁹)⁴ eV⁴ = 4×10⁻¹¹ eV⁴. So actually the value matches the author's stated 2.8×10⁻¹¹ eV⁴ to within a factor of 1.5 — *consistent*. But then the author claims that the "natural ALP range" m_a ∈ [10⁻²², 10⁻¹⁵] eV gives overshoot of 22–36 orders of magnitude. Let's check: at m_θ = 10⁻²² eV, the overshoot is (m_θ/H₀)² = (10⁻²²/10⁻³³)² = (10¹¹)² = 10²². ✓. At m_θ = 10⁻¹⁵ eV: (10⁻¹⁵/10⁻³³)² = 10³⁶. ✓. So the arithmetic checks out, but the author's "rigidity" argument depends on holding α/M fixed at the one-loop value, which they then admit can be floated. This makes R4 closure a moving target.
**Required fix:** Acknowledge that with α/M free, R4 is not closed at all; this is what the text already says in Sec. IV D, but the abstract still claims all four routes close at amplitude level.

### P1A-M9: γ_PTA prediction — derived from companion analysis cited as published
**Location:** Sec. X G (p. 15), Table IV (p. 20).
**Problem:** "γ = 2.567 ± 0.382 from real-KDE re-analysis of the 15-yr free-spectrum data (GPU MCMC, companion Paper III [46])" — load-bearing claim with specific 3-digit precision from an unpublished companion. The body claim that matter-bounce γ = 3.0 sits at "+1.13σ" depends on the cited 0.382 σ. Cannot be refereed without access to Paper III.
**Required fix:** Either supply the analysis or remove the claim.

### P1A-M10: NANOGrav OmegaGW comparison declared deferred
**Location:** Sec. IX L, p. 13.
**Problem:** Barrier 12 cites Ω_GW ≲ 0.07–0.17 at the bounce, then immediately says "A quantitative comparison to NANOGrav requires propagating the bounce GW spectrum through the transfer function to the nHz band, which is deferred to a forthcoming bounce-GW dedicated paper (deferred); for the present analysis, Barrier 12 closes as a global energy-density-fraction ceiling rather than a direct NANOGrav exclusion." So this barrier does not actually close anything — it cites a ceiling that is not compared to data. Including this as one of the "13 (or 14)" structural barriers inflates the count.
**Required fix:** Either complete the analysis or remove from the barrier count.

### P1A-M11: LiteBIRD ~9σ vs 0.73σ confusion in Conclusions
**Location:** Sec. XV, p. 18.
**Problem:** The text reads "LiteBIRD ... detects non-zero β at ∼ 9σ (a 0.27°/0.03° overall sensitivity number). The relevant model-discrimination test, however, is the differential against the prior central value β_obs = 0.342° ± 0.094°: LiteBIRD will distinguish the spectator-ALP-derived 0.27° from the observed 0.342° at |0.342 − 0.27|/√(0.03² + 0.094²) ≈ 0.072°/0.0987° ≈ 0.73σ, NOT at the naive |0.342 − 0.27|/0.03 = 2.4σ." This admits the headline 9σ is the wrong test, the right test gives 0.73σ, and even a 2.4σ figure (still wrong) is dismissed. Including the 9σ at all in a Conclusions section is misleading. The actual model-discrimination capability is sub-1σ.
**Required fix:** Lead with the 0.73σ number. Drop the 9σ as a "sensitivity number" — it tests a hypothesis nobody disputes.

### P1A-M12: The "70 OOM galaxy spin underprediction" is not a result
**Location:** Sec. II C 2, Sec. III B, Sec. XIV B.
**Problem:** "underpredicts any plausible spin asymmetry by > 100 orders of magnitude" appears multiple times as if this is a triumph. Underpredicting an effect by 100 orders of magnitude means the theory makes no prediction in this channel — this is consistency with null, not a positive test result. It does not narrow ECH parameter space because the relevant parameter space is already infinitesimal in this channel.
**Required fix:** State plainly that this channel does not test ECH.

### P1A-M13: "Channel-level vs operator-level" distinction not clearly defined
**Location:** Throughout — abstract, Sec. I, Sec. IV.
**Problem:** The paper repeatedly hedges "channel-level" closure vs. "operator-level" closure. The reader is never told the precise definition of "channel" vs. "operator" in EFT terms. Are the four "channels" four classes of operators? Four physical mechanisms? Four observational signatures? Without a clean definition the hedge becomes a get-out-of-jail-free card.
**Required fix:** Define "channel" and "operator-level closure" precisely in Sec. I or Sec. IV.

### P1A-M14: Pontryagin density "generically non-zero pointwise but a total derivative"
**Location:** Sec. X B (p. 14), Sec. X D, abstract.
**Problem:** This claim is the centerpiece. The author correctly notes RR̃ = ∂_μ K^μ is a total derivative locally. But on a *closed* manifold without boundary, ∫RR̃ is a topological invariant (the Pontryagin number) which can be non-zero. The claim that the Holst sector "contributes only a boundary term to the action" assumes the boundary or topological term is irrelevant. For closed FRW spatial slices this needs justification. More importantly, for cosmological perturbations on a Euclidean R³ background with appropriate falloff, RR̃ is indeed a boundary term — but the paper should state this assumption explicitly. As written the proof glosses over the topological subtlety.
**Required fix:** State the topology/falloff assumptions explicitly. Acknowledge the topological term as a potential exception.

### P1A-M15: "If matter includes fermions" caveat undermines transparency theorem scope
**Location:** Sec. X E, p. 14.
**Problem:** The transparency result fails if "(1) matter includes fermions with nonzero spin density." But the real universe contains fermions. The Standard Model contains fermions. The whole point of ECH coupling fermions to gravity is that fermions have spin density. The theorem applies only to "canonical scalar matter," which is a vacuum-inflaton sector — and is admitted to be inapplicable as soon as one includes the matter content needed for cosmology. The paper does not state this prominently enough.
**Required fix:** Make explicit in the abstract that the perturbation transparency does *not* apply once Standard Model fermions are present, and discuss whether the inflaton-dominated era (where it might apply) is the relevant test regime.

### P1A-M16: Eq. (4) and Eq. (13) — γ²/(γ²+1) factor inconsistency with abstract
**Location:** Eq. (4) (p. 5), Eq. (13) (p. 9).
**Problem:** Eq. (4) gives the four-fermion interaction with coefficient γ²/(γ²+1), but Eq. (13) (Route 1 closure) shows the NJL term without the γ²/(γ²+1) factor — using just the Hehl–Datta κ. The abstract mentions a "parity-odd four-fermion partner ... with γ_BI/(γ²_BI + 1) · 8πG coefficient" as an *omitted* operator. So which is it — is Eq. (4) the parity-even or parity-odd combination? The notation γ²/(γ²+1) suggests parity-even (the parity-odd partner carries γ/(γ²+1) per the Freidel–Minic–Takeuchi paper), but this is not stated. The abstract treats the parity-odd four-fermion partner as missing from the analysis; Eq. (4) appears to include the parity-even version. This needs disambiguation.
**Required fix:** Clarify which γ-dependent combination is in Eq. (4) and which is omitted.

### P1A-M17: "Parameter Immunity (Barrier 7)" is not really a barrier
**Location:** Sec. IX G, p. 12–13.
**Problem:** "γ is fixed by the LQG area spectrum at a universal value; there is no mechanism within LQG to produce a landscape of γ values from which selection could operate." But the paper itself (Eq. 2 and surrounding text) acknowledges that γ varies across counting schemes by ~factor 2 (0.127 to 0.274 to 0.2375). So γ is *not* universally fixed — it depends on the entropy-counting scheme. Calling this a "barrier" is dubious.
**Required fix:** Reconcile with the γ-scheme-dependence discussion on p. 5.

### P1A-M18: "Liouville Conservation (Barrier 9)" — known result repackaged
**Location:** Sec. IX I, p. 13.
**Problem:** "Phase-space volume conservation prevents irreversible selection among post-bounce states from pre-bounce dynamics." This is a textbook result, not an ECH-specific constraint. Listed as a "barrier" it inflates the count. The author tags it as "known" in the classification — but then why is it in the catalog?
**Required fix:** Either justify ECH-specificity or remove.

### P1A-M19: "Decoupling Universality (Barrier 11)" and "Gravitational Democracy (Barrier 13)" — same content
**Location:** Sec. IX K and Sec. IX M, p. 13–14.
**Problem:** Both barriers say "torsion couples democratically/universally to matter species and cannot preferentially do X." These are the same physics applied to different downstream outcomes. The catalog should count once.
**Required fix:** Merge.

### P1A-M20: Abstract phrase "definitively erased ... at SPHEREx-accessible comoving wavenumbers"
**Location:** Abstract, p. 1.
**Problem:** "Definitively erased" is a strong claim. The actual argument is that e^32 push to subhorizon erases the bispectrum signal. But the e^32 push is only present if Ntot ≈ 92 is the right e-fold count, which is itself derived from a phenomenological ansatz the author admits is not a derivation (Appendix B). "Definitively" is overclaim.
**Required fix:** Replace with "would be erased under the e-fold count required by the ansatz."

---

## MINOR findings

### P1A-Mi1: Date in title block "Dated: June 2, 2026 PDT"
**Location:** p. 1.
**Problem:** Future date implies pre-print review draft.
**Required fix:** Standard.

### P1A-Mi2: PACS codes are deprecated
**Location:** p. 1.
**Problem:** PACS classification scheme is discontinued. Use current PRD subject classification.
**Required fix:** Replace.

### P1A-Mi3: Reference [44] cites arXiv:2603.13924
**Location:** Refs, p. 21.
**Problem:** arXiv:2603.13924 — month "26" is invalid; arXiv uses YYMM format. This is either a typo or a fabricated reference.
**Required fix:** Verify and correct.

### P1A-Mi4: "Hubify-Projects/bigbounce" repository in published manuscript
**Location:** p. 5 and Data Availability section.
**Problem:** Unconventional. GitHub repos are acceptable but should be archived (Zenodo with DOI) for permanence.
**Required fix:** Provide archived DOI.

### P1A-Mi5: Reference [22] mismatched (Sec. IV B coefficient discussion)
**Location:** p. 7.
**Problem:** Mercuri & Capozziello [22] is cited for "αem/(4π) appearing in Eq. 14" but Eq. 14 is the *author's* one-loop ansatz, not derived in [22]. The author admits this on p. 9 ("no published calculation currently derives this exact coefficient structure"). Then why is [22] cited?
**Required fix:** Cite [22] only for the classical Holst+fermion construction, not for the loop coefficient.

### P1A-Mi6: Excessive use of "the ... is" passive constructions, run-on parenthetical hedges
**Location:** Throughout.
**Problem:** Sentences run 8–12 lines with nested parentheticals. The abstract has a 7-line sentence ending "(the relative e-fold differential between bounce and CMB horizon-exit; comoving wavenumbers k are constant by definition and only physical scales scale with a⁻¹ ∝ e⁻ᴺ), deep inside the inflationary subhorizon regime carrying purely vacuum-inflationary fluctuations rather than matter-bounce contraction modes)". This is unreadable.
**Required fix:** Edit for clarity.

### P1A-Mi7: "We treat this scaling explicitly as an ansatz, not a derivation" — appears 4+ times
**Location:** Abstract, Sec. I, Sec. II C, Appendix B.
**Problem:** Saying it once is honest; saying it four times is signaling that the author knows it's a problem.
**Required fix:** Consolidate.

### P1A-Mi8: Figure 1 dashed-box caption text
**Location:** Fig. 1 caption, p. 4.
**Problem:** "ECH appears bordered with a dashed box marked channel-level closure under stated assumptions (this paper)—the 14-constraint catalog narrows the four enumerated minimal-ECH dark-energy channels to zero phenomenologically free pathways within those channels." Then footnote a (Table I) says "not solved." Same content paragraphed differently — pick one.

### P1A-Mi9: Eq. (2) "γSU(2) ≈ 0.274"
**Location:** p. 5.
**Problem:** The standard SU(2) full-counting result is γ = 0.23753... (Meissner 2004), not 0.274. The author has two different SU(2) values floating: 0.274 (called "the refined SU(2) full counting") and 0.2375 (called "Domagała–Lewandowski–Meissner refinement"). Both Meissner and DLM are SU(2) refinements. The 0.274 value is from earlier Ashtekar et al. work. The taxonomy is wrong.
**Required fix:** Verify which counting gives 0.274 vs 0.2375; the citation map in the text [17,18] is to DLM and Meissner respectively, both of which give ~0.2375, not 0.274.

### P1A-Mi10: Acknowledgments list "for the A(z) comparison" — unexplained
**Location:** p. 18.
**Problem:** Lior Shamir thanked for "aggregate CW/CCW galaxy spin counts for the A(z) comparison." But the A(z) comparison is not described in this paper (it's in Paper IV, "in preparation"). Why acknowledge a contribution to a different paper here?
**Required fix:** Move to the appropriate companion paper.

### P1A-Mi11: ~0.27° vs 0.342° — which is "the ECH prediction"?
**Location:** Throughout — abstract says ~0.27°, Conclusions says 0.27° as spectator-ALP-derived prediction.
**Problem:** The 0.27° comes from where? It is described as "a benchmark consistency point." The actual measurement is 0.342° (Eskilt–Komatsu) or 0.215° (ACT). 0.27° is between them. The author never derives 0.27°; it appears to be chosen as a round-number midpoint. Calling it "consistent with the WMAP+Planck 1σ band" is technically true but somewhat hollow if 0.27° is simply chosen.
**Required fix:** Either derive 0.27° from a specific ALP model with stated parameters, or replace with "a value within the observed 1σ band."

### P1A-Mi12: Sec. VIII (Related Work) cites Liu et al. [41] as showing "EC torsion fits the S8 tension"
**Location:** p. 12.
**Problem:** This is presented as supporting evidence but the present paper's MCMC analysis (cited from companion) finds ΛCDM+∆Neff ≈ 0 and "Recovers ΛCDM." If EC torsion fits S8 (i.e. provides new physics) but the present paper finds no new physics, these are in tension.
**Required fix:** Reconcile or remove.

### P1A-Mi13: Pop ławski misspelled as "Pop lawski" throughout
**Location:** Refs, body, ack.
**Problem:** Proper rendering of "Pop ławski" (Polish ł) failed in the LaTeX rendering — appears as "Pop lawski" with space. Cosmetic but consistent.
**Required fix:** Use `\l` macro or ł character.

### P1A-Mi14: Eq. (12) C^EB_l formula
**Location:** Sec. III A, p. 7.
**Problem:** The standard rotation-induced birefringence formula at linear order in β is C^EB_l = (1/2) sin(4β) (C^EE_l − C^BB_l), reducing to 2β(C^EE − C^BB) only for small β. Author uses the small-angle form correctly but should note linearization.
**Required fix:** Note linearization explicitly.

### P1A-Mi15: Sec. XIII numerical inconsistency
**Location:** p. 16.
**Problem:** "fNL = −35/8 ... SPHEREx parameter sensitivity (bispectrum-only σ(fNL) ≈ 0.7 from Heinrich et al. 2024, leading to 3–5σ post-systematic-budget significance)". With fNL = 4.375 and σ = 0.7, raw significance is 6.25σ. Even degraded to σ = 1.0, it is 4.4σ. The "3σ" floor never appears in the arithmetic.
**Required fix:** Reconcile with E6.

---

## NITs

### P1A-N1: "is a phenomenological ansatz" appears 11+ times
Frequency of hedge wording suggests anxious authorship.

### P1A-N2: "ECH" / "Einstein-Cartan-Holst" used inconsistently with and without hyphens.

### P1A-N3: "channel-level closure under stated assumptions" — phrase repeats verbatim 6+ times.

### P1A-N4: Table IV "1σ statistical or theoretical error" wording in caption-adjacent footnote is awkward.

### P1A-N5: "Recovers ΛCDM" (Table I) — colloquial; "consistent with ΛCDM" preferred.

### P1A-N6: Footnote 1 (p. 11) spans nearly half a page; consider promoting to a subsection.

### P1A-N7: Eq. numbering: Sec. IV B refers to "Eq. 14" but Eq. (14) is in Sec. IV B itself — internal forward references are inconsistent.

### P1A-N8: Bibliography uses both "physical review d 53, 5966" lowercase and "Physical Review D ..." Title Case inconsistently.

---

## Length assessment

The paper is 21 pages for what is essentially: (i) the perturbation-transparency observation (Sec. X, ~1.5 pages); (ii) a tabulated list of obstructions to a dark-energy mechanism the author admits is not derivable from first principles (Sec. IX, ~2 pages); (iii) four channel-amplitude-budget calculations with admitted dimensional pathologies (Sec. IV, ~3 pages); and (iv) extensive narrative around the limitations of all of the above.

A focused PRD paper containing the perturbation-transparency theorem alone, with the four-route amplitude-budget calculations as a discussion section, would be ~8 pages. **Recommended maximum: 10 pages.**

The remaining 11 pages are: (a) repetitive hedging language, (b) companion-paper cross-references, (c) review-log residue ("supersedes earlier draft", "actively running MCMC chain"), (d) "structural barrier" cataloging that double-counts and triple-counts the same physics, and (e) two figures that are not analyzable.

---

## Summary recommendation

**REJECT**

This paper cannot be accepted in PRD in its current form. The central claim — a "channel-level closure of four minimal ECH dark-energy routes" — is internally undermined by the author's own admissions: the operator basis is incomplete (two operators explicitly excluded from the abstract), the dimensional analysis underlying the ρ_Λ identification is broken (Appendix B states the operator is +1 off-shell mass dimension, three short of what's required, "fixed" by an on-shell scaling ansatz), Route 4 is acknowledged mid-paper to be a "naturalness objection" rather than an amplitude closure, the 13/14 barrier counting is self-contradictory, and the load-bearing numerical results (MCMC posteriors, SPHEREx forecasts, PTA spectral index, ALP fits) are all cited from companion papers "in preparation." The perturbation-transparency observation (Sec. X) is genuine and worth ~1.5 pages, but is presented as part of a much larger structural-closure claim that the manuscript does not establish. The abstract overclaims, the figures contain content the captions disclaim, the tables show MCMC values from unpublished sources, and the body contains review-log residue ("supersedes earlier draft," "actively running on a dedicated MPI pod"). I recommend the author extract the perturbation-transparency result as a focused short paper (≤10 pages) with the four-route discussion as a single analysis section, drop the "channel-level closure" framing entirely, post the companion papers to arXiv before resubmission, and have the dimensional analysis in Appendix B independently checked. As submitted, this is not a PRD-quality manuscript.