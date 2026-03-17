# Paper 1.2 — Simulated Referee Reports

**Date:** 2026-03-14
**Paper:** "Geometric Dark Energy: Phenomenological Viability, Systematic Closures, and Requirements for Completion"

---

## REFEREE A — Sympathetic but Rigorous

### Summary

The paper presents a dark-energy framework based on Einstein-Cartan-Holst gravity, performs MCMC fits to current cosmological data, then systematically tests five routes to deriving the late-time equation of state w = -1 from first principles. All five routes fail. The paper extracts structural lessons from these failures and formulates decision rules (DR1-DR5) for future geometric dark-energy models. The central new finding is a "mass-coupling lock" in Poincare gauge theory: making a torsion mode cosmologically light simultaneously suppresses its matter coupling to irrelevance.

### Major Strengths

1. **Intellectual honesty is exceptional.** The paper explicitly labels w = -1 as assumed rather than derived, classifies its observational claims as "consistency checks, not predictions," and includes a claims classification table (Appendix C) separating derived, assumed, fit, and retired claims. This level of self-scrutiny is rare and admirable.

2. **The mass-coupling lock is a genuine structural insight.** The general canonical-normalization argument (Section 6.6) is clean and compelling: if L = -Z(dφ)²/2 - μ²φ²/2 + gφJ, then canonical normalization locks m and g_eff together. The PGT demonstration is concrete, and the Brans-Dicke analogy strengthens the case. The W boson counterexample showing how the lock is evaded is pedagogically effective.

3. **The decision rules framework (DR1-DR5) is useful.** These are not vague aspirations but concrete, testable requirements grounded in demonstrated failure modes. DR5 in particular is a previously unrecognized constraint that will be immediately useful to anyone working on geometric dark energy.

4. **The closure methodology is reproducible.** Predefined gates, kill criteria frozen before computation, and documented negative results set a standard for how theoretical model testing should be reported.

### Major Weaknesses

1. **Part I is a standard ΛCDM+ΔNeff analysis.** The MCMC results are solid but not distinctive. The verification analysis (Table II) actually undermines the original tension-reduction claims by finding ΔNeff consistent with zero and H₀ consistent with Planck ΛCDM. The paper acknowledges this honestly (lines 362-367) but a reader might wonder why Part I needs 7 pages if the result is "consistent with ΛCDM."

2. **The scaling ansatz (Eq. 3) is underdeveloped.** The paper claims fine-tuning reduction from 10^120 to 10^5, but the ansatz ρ_Λ ≈ Ξ M_Pl⁴ requires choosing α/M and N_tot to match observations. The "reduction" is parametric, not mechanistic — the paper trades one unexplained number (Λ) for another (N_tot ~ 92). The fine-tuning comparison table (Table IV) is misleading because the ECH entry's "natural scale" already contains the answer.

3. **The companion technical note is load-bearing but unavailable.** The closures of Track B, Branch G, Route T1, and Route S1 are summarized but not fully derived in this paper. A referee must take these closures on trust or request the companion note. For a paper whose primary contribution is the closures, this is a significant weakness.

### Questions for the Authors

1. The verification analysis finds ΔNeff = -0.020 ± 0.169 (full tension) and +0.065 ± 0.17 (Planck+BAO+SN), both consistent with zero. Given this, what is the phenomenological content of the framework beyond standard ΛCDM? Please clarify what the framework adds that a generic ΔNeff extension does not.

2. In the mass-coupling lock argument, you state that Z ∝ |t₃| and μ² ∝ M_Pl² "producing exactly this structure." Can you provide the explicit derivation showing how the PGT quadratic action maps to the Z, μ, g parameterization? This is the key step connecting the general argument to the specific model.

3. Is Foundation B (metric-affine Nieh-Yan) genuinely distinct from Route T1, or is it the same mechanism in a different gauge group? You flag this risk yourself ("This may be Route T1 in better clothing"). Has the first check been performed?

4. The paper cites Golden2026v1 as a superseded preprint. Is this available? What specific claims from v1 have been retired, beyond those listed in the claims table?

### Verdict

**Minor revision.** The paper makes a genuine contribution through the mass-coupling lock and the DR framework. The phenomenology section could be shortened, the companion note should be made available, and the scaling ansatz limitations need clearer acknowledgment. With these revisions, the paper merits publication in PRD.

---

## REFEREE B — Skeptical Theorist

### Summary

The author presents a phenomenological dark-energy model based on Einstein-Cartan-Holst gravity, acknowledges that the model's central assumption (w = -1) cannot be derived from first principles within the minimal framework or its most natural extension (PGT), and attempts to extract value from this negative result by formulating "structural lessons" and "decision rules." The main claim is that a "mass-coupling lock" prevents propagating torsion from serving as a dark-energy mechanism.

### Major Strengths

1. The paper is honest. This is its primary virtue. Most papers in this subfield overclaim; this one does the opposite, which I respect.

2. The MCMC analysis is competent and independently verified.

3. The mass-coupling lock observation, while simple, is correct and worth stating for the PGT case.

### Major Weaknesses

1. **The paper does not contain a result in the traditional theoretical physics sense.** The mass-coupling lock is a straightforward consequence of canonical normalization — any graduate student who writes down the canonically normalized PGT action would observe this. The paper elevates this observation to a "structural insight" and a "previously unrecognized constraint," but it is simply what happens when you canonically normalize a field whose kinetic term and mass both depend on the same coupling. The Brans-Dicke analogy (ω_BD → ∞ is the GR limit) has been known for 60 years.

2. **The generality claim is overstated.** The paper presents the lock as a constraint on "any geometric dark-energy theory" where mass and coupling share a common origin. But the very next paragraph lists three evasion mechanisms (Higgs, gauge symmetry, environmental). So the constraint applies to the specific class of theories where no independent mass-generating mechanism exists. This is less a structural insight than a statement about model building: "if you want a light field that couples to matter, give it an independent mass." This is known.

3. **The closure program is self-referential.** The four minimal routes are defined, tested, and closed within the same paper (with details deferred to a companion note). There is no independent verification. The routes chosen may not be exhaustive, and the "kill criteria" are the author's own. The closures are therefore only as strong as the author's choice of what to test and when to stop.

4. **The paper reads as a literature review with MCMC attached.** Parts II and III contain no new calculations. The Fierz rearrangement (Track B) is textbook. The one-loop argument (Branch G) is a citation of Vassilevich. Route T1 cites Calcagni-Mercuri. Route S1 is an assessment. The PGT mass formula cites Sezgin-van Nieuwenhuizen and Karananas. The paper's original content is the synthesis and the framing, not the calculations.

5. **The phenomenological framework has no predictive power.** w = -1 is assumed. ΔNeff is consistent with zero. Birefringence requires an assumed coupling. Galaxy spin is unconnected. The "fine-tuning reduction" replaces one free parameter (Λ) with another (N_tot). What does this framework predict that ΛCDM does not?

### Questions for the Authors

1. What specific calculation in this paper is new? Please identify the equations that appear here for the first time in the literature.

2. The mass-coupling lock is presented as a "previously unrecognized constraint." Has the author searched the PGT literature for prior statements of this observation? The relationship between kinetic normalization, mass, and coupling in PGT has been discussed by Yo and Nester, by Blagojević, and by others. Please demonstrate that this observation is genuinely new.

3. You state that the closures "map the theory landscape." But you have tested four routes in one model class and one extension. How is this a landscape map rather than a case study?

4. DR4 ("Fails cleanly if it doesn't work") is a methodological standard, not a physics requirement. Why is it listed alongside physics requirements DR1-DR3 and DR5?

5. What is the minimum result that would make the framework publishable as more than phenomenology? You list four conditions in Section 9.4 — can the author commit to testing any of them?

### Verdict

**Major revision or rejection.** The paper is honest and well-organized but lacks a sufficiently original theoretical result for PRD. The mass-coupling lock is an observation, not a derivation. The MCMC analysis adds nothing beyond standard ΔNeff extensions. The paper might be suitable for a review journal (e.g., Symmetry, Universe) or as a companion to a paper that actually derives something new. In its current form, the contribution is insufficient for a regular PRD article.

---

## REFEREE C — Technical Nitpicker

### Summary

This paper analyzes a dark-energy model based on Einstein-Cartan-Holst gravity, tests several derivation routes, and proposes structural constraints for future geometric dark-energy models. The analysis combines MCMC parameter estimation with theoretical model assessment.

### Major Strengths

1. Clear three-part structure with well-delineated phenomenological, theoretical, and programmatic sections.
2. Independent MCMC verification with publication-quality convergence diagnostics.
3. Claims classification table (Appendix C) is a useful reference.

### Major Weaknesses

1. **Inconsistent H₀ values.** The original analysis reports H₀ = 69.2 ± 0.8 (Eq. 6, tension dataset) while the verification reports H₀ = 67.68 ± 1.06 (Table II, full-tension). These are nominally the same dataset class but differ by 1.5 km/s/Mpc. The paper attributes this to the SH0ES prior (line 366-367), but the discrepancy is not fully explained. Are the original and verification analyses using the same SH0ES prior? If yes, why do they disagree? If no, this should be stated explicitly. The footnote in Appendix B ("Original values from the tension dataset (includes SH0ES H₀ prior)") does not resolve this because the verification also includes a "full-tension" dataset.

2. **Eq. (9) is approximate but used as exact.** The canonically normalized coupling g_eff ~ 1/(M_Pl √|t₃|) is stated with a "~" sign, but the 10²⁹ suppression number is presented as a precise conclusion. What is the O(1) coefficient? The mass formula m_B = M_Pl/(4√(π|t₃|)) has the factor 4√π. What is the corresponding exact expression for g_eff?

3. **DiegoPalazuelos2025 citation is incomplete.** Reference [18] reads "P. Diego-Palazuelos and E. Komatsu, (2025)" with no journal, arXiv ID, or title. This citation is used to support the 3.9σ combined birefringence detection, which is a quantitative claim. An incomplete citation for a quantitative result is not acceptable.

4. **Legner2025 arXiv ID may be incorrect.** The arXiv ID 2507.09228 has a submission date of July 2025, which is after the nominal paper date. Please verify this is the correct reference and update accordingly.

5. **The fine-tuning comparison table (Table IV) is misleading.** The "Natural Scale" column lists (α/M)D_inf M_Pl⁴ for the ECH model, which already incorporates the suppression mechanism. By this logic, any model can achieve low fine-tuning by defining its natural scale to include whatever suppression factor produces the observed value. The comparison should use a common standard (e.g., the ratio of the predicted scale to the observed scale before any tuning).

6. **Notation inconsistency.** The Barbero-Immirzi parameter is denoted γ throughout but appears as BI in the abstract when written in non-LaTeX contexts. The claims table (Appendix C) refers to "BI < 1" rather than "γ < 1." Also, the paper uses both "Poincaré gauge theory" and "PGT" before PGT is formally defined (it first appears in the abstract but is only defined in the introduction).

7. **Missing error propagation.** The fine-tuning score "~10⁵" is quoted without uncertainty. Given that it depends on α/M (fit parameter with unstated uncertainty) and N_tot (assumed ~92, no error bar), how sensitive is this score to parameter variations? The Monte Carlo scan is mentioned but its detailed results are not shown.

### Questions for the Authors

1. Please provide the exact expression for g_eff in the canonically normalized PGT theory, not just the parametric scaling. What is the numerical coefficient?

2. The paper states R̂-1 < 0.01 as the convergence criterion (line 315) but Table II reports R̂-1 = 0.001 and 0.003. Were different convergence thresholds used for the original and verification analyses?

3. Table III reports χ²_eff = 1148.3 for the ECH model. How many data points are in the full-tension dataset? Without this, the goodness of fit cannot be assessed.

4. The "perfect-square structure" of L_4f (line 230) is credited to the companion note [21]. Can the author show this structure here, or at minimum state the identity being used?

5. Line 197-199 states the Holst term is "classically equivalent to a topological term (the Nieh-Yan density) on shell." This is imprecise: the Holst term differs from the Nieh-Yan density by a torsion-squared term. On shell (when torsion vanishes in vacuum), they agree, but in the presence of matter (torsion ≠ 0), they differ. Please clarify.

6. In Appendix A, the definition ρ_Λ = Λ_eff M_Pl²/(8π) combined with ρ_Λ ≈ (2.3 meV)⁴ implies Λ_eff ≈ 1.1 × 10⁻⁵² m⁻², but the paper elsewhere uses ρ_Λ = Ξ M_Pl⁴ (Eq. 3). These two parameterizations are consistent but could confuse readers. Please unify notation.

### Verdict

**Minor revision.** The paper is well-structured but has several technical issues that must be addressed before publication. The incomplete citation [18] is the most serious — it must be resolved. The H₀ discrepancy between original and verification analyses needs explicit explanation. The approximate nature of Eq. (9) should be acknowledged or corrected. With these fixes, the paper is acceptable for PRD.

---

## Cross-Referee Summary

| Issue | Referee A | Referee B | Referee C |
|-------|-----------|-----------|-----------|
| Part I too standard | Mild concern | Strong objection | Not raised |
| MCL originality | Accepts as insight | Disputes novelty | Accepts, wants exact form |
| Closure methodology | Positive | Self-referential | Neutral |
| Missing companion note | Concern | N/A | N/A |
| Predictive power | Mild concern | Strong objection | N/A |
| Technical accuracy | N/A | N/A | Several issues raised |
| Publication merit | Minor revision | Major revision/reject | Minor revision |

**Consensus weakness:** The paper's contribution rests almost entirely on the mass-coupling lock and the DR framework. If a referee does not find these sufficiently original (Referee B's position), the paper has no fallback. The phenomenology alone does not warrant publication.

**Consensus strength:** The honesty and self-scrutiny are unanimously praised. The paper does not overclaim.
