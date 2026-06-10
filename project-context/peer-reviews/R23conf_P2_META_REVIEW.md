# P2 R23conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 384.4s

---

META-REFEREE REPORT — new issues not caught by the five prior reviews

P2-META-E1 — Self-cancelling definition of BNL makes the coefficient-null-space analysis logically inconsistent
- Severity: ESSENTIAL
- Location: Sec. II.A, Eq. (1)–(2), p. 3–4; Fig. 1/Tab. I usage of BNL
- Why missed: Prior reviews flagged Eq. (2) as ambiguous, but none noticed that Eqs. (1)–(2) as printed imply algebraic cancellation of the very polynomial whose coefficients the paper later varies.
- Problem: Eq. (1) defines AT(k1,k2,k3) = (3 / (256 k1^2 k2^2 k3^2)) P(k1,k2,k3). Eq. (2) then defines BNL ≡ (10/3) P / (AT Σi k_i^3). With these two equations as written, P cancels out of BNL, so BNL would depend only on k1, k2, k3 (not on the six coefficients c1–c6). That directly contradicts the later claims that (i) different (c1,…,c6) choices change BNL(k1,k2,k3), (ii) the null-space scan yields r ranging 0.55–1.14, and (iii) the shape is only approximately local. In short, the current algebra makes the coefficient variation irrelevant to BNL, which cannot be what the authors intend.
- Required fix: Disambiguate notation and correct the formula. Either (a) AT in Eq. (2) is not the same AT as in Eq. (1), or (b) P in Eq. (1) is not the same as the P in Eq. (2), or (c) Eq. (2) has missing parentheses/factors (e.g., AT should be something like Σi k_i^3 or k_t^3 in the denominator, not the AT of Eq. (1)). Rewrite Eq. (2) explicitly (with units) so that BNL retains its dependence on the degree‑9 polynomial and thus on (c1,…,c6). Then verify that the benchmark values in Table I and the r-distribution from the null-space scan are reproduced by the corrected formula.

P2-META-E2 — Bayes factors are computed with σ = 0.7 but ignore the template-mismatch rescaling σ(fbounce) = σ(local)/r stated in Eq. (5)
- Severity: ESSENTIAL
- Location: Sec. VI.C, pp. 9–11; Table II p. 11; Table III p. 14
- Why missed: Reviewers checked the closed-form integral (Eq. 7) but not the consistency with Eq. (5)’s σ-rescaling.
- Problem: The paper states fmeasured = r fbounce and σ(fbounce) = σ(flocal)/r (Eq. 5), but the Bayes-factor section repeatedly uses “a mock SPHEREx detection at fNL = −4.375 (σ = 0.7).” If the survey’s σ = 0.7 is for the local-template parameter, the corresponding σ for the bounce amplitude should be 0.7/r ≈ 0.83 (with r ≈ 0.84). Using σ = 0.7 overstates all Bayes factors (e.g., the analytic delta-vs-uniform BF ~7 becomes ~6.2 when σ = 0.83). Every BF and “P(BF > 3)” that assumes σ = 0.7 must be recomputed or explicitly justified as being in the local parameterization (with the hypotheses and priors defined in that same parameter).
- Required fix: Recompute the Bayes factors using σeff = 0.7/r for the bounce amplitude, or explicitly redefine the model comparison entirely in the local-template parameter space (and then do not interpret BF as evidence on the bounce amplitude without the r mapping). Update Table II/III and the abstract’s BF envelope accordingly.

P2-META-M1 — Null-space sampling measure is ad hoc and basis-dependent; results on r-distribution are not invariant under reparametrization
- Severity: MAJOR
- Location: Sec. II.A, p. 3–4 (null-space SVD paragraph and footnote 1), and the abstract’s “±0.13 in r” systematic
- Why missed: Prior reviewers focused on arithmetic, not on the measure used in the null-space.
- Problem: The 10,000-sample null-space scan uses a uniform Euclidean ball of “radius 50” in coefficient space around a chosen reference solution. This measure is arbitrary, basis-dependent, and not tied to a physical metric (e.g., an induced Fisher metric on shape space). Although the text briefly says the radius/measure are “conventional choices,” the ±0.13 absolute scatter in r from this scan is then used in the systematic budget. Because the measure is not invariant to reparametrization of the six monomials (or a rotation within the null space), both the quoted r scatter and the [0.55, 1.14] extremal values can change under an equally valid basis choice.
- Required fix: Either (a) define and use a physically motivated, basis-invariant measure on the null space (e.g., whitened by the survey’s bispectrum Fisher metric so that sampling is in units of equal impact on the data), and report r-distributions under that measure; or (b) demote the ±0.13 and [0.55, 1.14] to purely illustrative numbers and remove them from the formal systematic budget. At a minimum, show sensitivity of the r-distribution to linear reparametrizations of (c1,…,c6) and to the sampling radius.

P2-META-M2 — Inconsistent use of the symbol BNL for two different constructs (local-limit nonlinearity vs. configuration-dependent shape amplitude)
- Severity: MAJOR
- Location: Sec. II.A (Eq. 2 calls BNL “the nonlinearity parameter in the squeezed limit”), Fig. 1/Tab. I (BNL evaluated away from the squeezed limit)
- Why missed: Earlier reviews flagged P-notation collisions but not this symbol-overloading.
- Problem: Eq. (2) introduces BNL as the (squeezed-limit) nonlinearity parameter, but Fig. 1 and Table I plot/quote BNL(k1,k2,k3) for equilateral and folded configurations as well. It is confusing to use the same symbol for: (a) the local-limit number (analog of fNL in the squeezed limit) and (b) a configuration-dependent normalized shape amplitude. This overloading makes it hard to follow later statements about “BNL varying from −4.375 to −2.25 across configurations.”
- Required fix: Use distinct symbols. For example, reserve fbounce ≡ limsqueezed BNL(k1,k2,k3) and introduce Sbounce(k1,k2,k3) for the configuration-dependent normalized amplitude (with Sbounce → fbounce in the squeezed limit). Update Fig. 1 and Table I labels, and rewrite Sec. II.A/III.B accordingly.

P2-META-M3 — The “singular-value bound” claim is mathematically unfounded
- Severity: MAJOR
- Location: Sec. II.A, p. 3–4 (“… the smallest-to-largest singular-value ratio is bounded below by the kinematic separation between the squeezed and equilateral configurations …”)
- Why missed: It reads like qualitative color; prior reviewers didn’t parse the linear algebra claim.
- Problem: The ratio σ3/σ1 of a 3×6 constraint matrix’s singular values is not “bounded below by kinematic separation” in any rigorous sense; it depends on the actual numeric rows, their scaling, and basis. The statement may mislead readers into thinking the rank/conditioning are controlled by “triangle separation,” which is not established here.
- Required fix: Remove this claim or replace it with a straightforward statement: e.g., “we find rank = 3 with σ3/σ1 ≈ 0.3 for our chosen benchmark rows,” without asserting a theoretical lower bound tied to kinematics.

P2-META-M4 — The Bayes-factor “probability” P(BF > 3) is undefined without specifying the sampling distribution of fobs vs nuisance priors, and the paper never does
- Severity: MAJOR
- Location: Table III, p. 14; Sec. VI.C pp. 9–11
- Why missed: Prior reviews focused on prior dependence and SSFSR precision, not on how P(BF>3) is computed.
- Problem: Table III reports “P(BF > 3)” entries (e.g., 96–98%) but does not define the probability space (draws over fobs? over nuisance parameters like σGR, multi-tracer efficiency, bϕ priors? both?). Without this, the numbers lack meaning and cannot be reproduced. This is particularly important because BF is highly sensitive to σ and priors; which distributions are driving P(BF>3) must be explicit.
- Required fix: Define P(BF>3) precisely: what variables are sampled, with what priors, and how many draws. Report the median and credible intervals across those draws (not just a scalar percentage). If these numbers are simply placeholders from one MC ensemble, say so and move them to an appendix with full details.

P2-META-m1 — “SPHEREx-like,” “LSS/SDB weighting,” “CMB Fisher” need explicit integral definitions to be reproducible
- Severity: MINOR
- Location: Sec. III.B, p. 6–7; abstract references
- Why missed: Prior reviews did ask for labeling and units in figures; none asked for the explicit weight definitions.
- Problem: The paper quotes distinct r values under “SPHEREx-like,” “LSS/SDB,” and “CMB Fisher” weightings. Without explicit formulas (e.g., W(k-triangle) ∝ …) and k‑range, another group cannot reproduce the quoted 0.829/0.830/0.835/0.876 values.
- Required fix: Provide the exact weighting kernels used (with equations), the triangle grids (kmin, kmax, binning), and normalization. A short table with the four weight definitions would suffice.

P2-META-m2 — The SPHEREx redshift range is inconsistent between sections (z ≈ 0.5–2 vs. 0.1–1.5) without justification
- Severity: MINOR
- Location: Sec. IV (SPHEREx sample z ≈ 0.5–2), Sec. IX.D (SDB joint Fisher over six bins z = 0.1–1.5)
- Why missed: Reviews noted the SDB section is subordinated but didn’t cross-check z-ranges.
- Problem: Different SPHEREx redshift ranges are used in different sections without stating why (bispectrum vs SDB). Since redshift coverage materially affects GR and bϕ systematics, the paper should justify the difference (e.g., “SDB test uses the six-bin low‑z subset of the full SPHEREx footprint for which [assumption] holds”).
- Required fix: Add one sentence clarifying the rationale for the different z-ranges and, if relevant, the impact on the quoted σ’s.

P2-META-m3 — Fermion/torsion caveat cites an operator but no bound; the text implies ΔNeff channels but provides no quantitative constraint
- Severity: MINOR
- Location: Sec. I–II.C, p. 2–5 (assumption (f))
- Why missed: Other reviews focused on bounce transmission assumptions; not on the torsion aside.
- Problem: The manuscript discusses the Hehl–Datta–Mercuri four‑fermion term ⟨ψγ̄5γaψ⟩^2 and says it can re‑activate torsion and affect scalar observables/ΔNeff. It then asserts the prediction is “robust within the scalar-only class” and that fermion energy density is “negligible,” but gives no bound (e.g., an upper limit on ⟨ψγ̄5γaψ⟩^2 or on a torsion-induced contribution to fNL). As written, the caveat is untestable and leaves readers unsure how to check whether (f) holds.
- Required fix: Either provide (or cite) a quantitative upper limit sufficient to justify that torsion effects are negligible for the SPHEREx‑scale fNL forecast, or explicitly state that this is an uncontrolled assumption outside the scalar‑only class and remove it from the “robustness” language.

P2-META-N1 — The “SVD rank is exactly 3” statement should specify the monomial normalization used
- Severity: NIT
- Location: Sec. II.A, p. 3–4
- Why missed: Others focused on numerical consistency, not reproducibility of the SVD.
- Problem: Conditioning and singular values depend on column scaling. To reproduce “σ3/σ1 ≈ 0.3,” a reader needs to know the monomial normalization. The text hints “in our reference monomial normalization” but does not define it.
- Required fix: Add a one-line definition (e.g., each monomial scaled by kmax^9 or unit‑variance normalization on the triangle set) so the SVD check is reproducible.

Meta-review recommendation
MAJOR REVISIONS

Rationale: In addition to the numerous essential/major issues already raised by the five referees, the self-cancelling BNL formula (P2-META-E1) conflicts with the core coefficient-null-space program, and the Bayes factor section systematically uses σ = 0.7 without the r-rescaling required by Eq. (5) (P2-META-E2). Both affect headline conclusions and must be corrected. The null-space measure/basis dependence (P2-META-M1) and symbol overloading (P2-META-M2) further undermine clarity and reproducibility.

Global blocker count and outlook
Aggregating all six reviews (the five prior plus this meta-review), I count at least 10 essential/major blockers that directly affect the main claims (normalization/convention consistency, Bayes-factor bookkeeping, σ-pipeline construction, Eq. (2) correctness, injection/estimator mismatch, prior dependence in the abstract, GR/bϕ propagation, κ1 range justification, and now the BNL self-cancellation and σ-rescaling in BF). If the authors systematically address these, I am moderately confident the paper can pass independent (non-bounce) peer review as a careful forecast/recast rather than as a discovery claim. However, the current draft requires substantial technical correction, clearer definitions, and a more disciplined treatment of priors and systematics before it can meet PRD standards.