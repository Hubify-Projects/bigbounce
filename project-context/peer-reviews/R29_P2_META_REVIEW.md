# P2 R29 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 276.3s

---

Meta-referee report (focus: blind spots none of the 5 reviewers caught)

P2-META-E1 — Definitional inconsistency that collapses the null‑space/mismatch program
- Severity: ESSENTIAL
- Location: Sec. II.A “The Prediction”, pp. 2–3, Eqs. (1)–(2) and the paragraph immediately after Eq. (2)
- Why missed: Each referee checked units and signs locally; none audited the P vs AT algebra end‑to‑end.
- Problem:
  • Eq. (1) defines AT(k1,k2,k3) = (3/256) k1^2 k2^2 k3^2 P(k1,k2,k3).  
  • Eq. (2) defines BNL ≡ (10/3) P / [AT Σi k_i^3] and claims “no cancellation of P occurs between Eqs. (1) and (2).”
  • But substituting Eq. (1) into Eq. (2) gives BNL ∝ P / [ (3/256) k1^2 k2^2 k3^2 P × Σk_i^3 ] = const × [k1^2 k2^2 k3^2 / Σk_i^3], i.e. the P cancels identically. If this is the intended definition, BNL cannot depend on the six polynomial coefficients, and the entire null‑space sampling, r‑distribution, and “template mismatch” exercise collapses.
- Required fix: Correct the definition. Either (i) BNL should be proportional to AT divided by Σk_i^3 (not P/AT), or (ii) AT in Eq. (1) is not proportional to P as written. Provide the exact Cai et al. mapping and re-derive every result (r, rcos, figures, and all downstream sensitivity/Bayes numbers) under the corrected definition. Without this, the central quantitative claims are not algebraically well-posed.

P2-META-E2 — Invalid 2D–3D cross‑channel “validation” of r
- Severity: ESSENTIAL
- Location: Sec. II (end of p. 5 into p. 6), “Injection/recovery test… KSW-type optimal linear estimator … SPHEREx photometric-z power spectra … full sky.”
- Why missed: Reviewers challenged statistics, but not the geometry/channel mismatch.
- Problem: The injection–recovery test uses a 2D, flat‑sky, CMB‑style KSW estimator with full‑sky geometry and then inserts a 3D SPHEREx photometric‑z power spectrum as a diagonal “noise covariance.” This mixes incompatible statistics (2D estimator, 3D survey noise, no window/mode‑coupling), so rmeas = 0.90 ± 0.01 is not a valid validation for a 3D galaxy‑bispectrum pipeline. The text concedes “not a full simulation pipeline,” but still uses the number as a supporting cross‑check.
- Required fix: Either remove this validation entirely or replace it with a 3D galaxy‑bispectrum estimator test using realistic SPHEREx tomographic bins and window, or an analytic cross‑Fisher between the bounce and local templates in the same 3D Fisher metric used by Heinrich et al.

P2-META-M1 — Ambiguous/likely incorrect symmetry-factor division in Appendix A
- Severity: MAJOR
- Location: Appendix A.1, Eq. (A7), p. 23; discussion of Sv
- Why missed: Other reviews did not scrutinize vertex‑level combinatorics.
- Problem: The bispectrum is written as Bζ = −2 Im Σv Σσ (1/Sv) Iv(σ), with Sv=2 for the ζ·ẋζ^2 vertex, Sv=1 otherwise. In standard in‑in/Wick counting, identical‑leg symmetry factors divide the interaction Lagrangian to avoid overcounting at the Feynman‑rule level; once you explicitly sum over S3 external permutations, inserting an extra 1/Sv generally double‑counts the division and suppresses the amplitude. No derivation is shown to justify 1/Sv here.
- Required fix: Show the explicit Wick expansion for one vertex (e.g., ζ·ẋζ^2) including internal identical‑leg factors and the S3 sum, and prove the 1/Sv factor is required in Eq. (A7). If it is not, remove 1/Sv and recheck the numerical benchmarks.

P2-META-M2 — “Basis‑independent shape cosine” claim is not true as stated
- Severity: MAJOR
- Location: Abstract p. 1 and Sec. II (pp. 3–5): “shape‑cosine stability rcos > 0.95 is basis‑independent”
- Why missed: Others questioned r’s basis dependence; none disentangled rcos language.
- Problem: rcos is computed as an unweighted Euclidean inner product over a chosen triangle grid; its value is invariant under reparameterizations of coefficient space only for a fixed shape function, but its distribution under sampling of a null space depends on the sampling measure, which is basis‑dependent (the authors themselves state the sampling measure for r is basis‑dependent). Calling the stability “basis‑independent” is therefore misleading unless you mean “invariant for any fixed coefficient set.”
- Required fix: Rephrase precisely: (i) clarify that “basis‑independent” refers to the shape cosine of a given coefficient set, not to the distribution over the null‑space induced by a chosen sampling basis; (ii) if the intention was a stronger claim, demonstrate invariance by sampling the null space under multiple linear reparameterizations and reporting rcos distributions.

P2-META-M3 — Mislabeling of “Fisher weights” (k² and 1/k²) that are not the actual Fisher kernels
- Severity: MAJOR
- Location: Sec. III.B, p. 8 (list of 10 weighting schemes: “CMB Fisher, w ∝ k²; LSS scale-dependent-bias, w ∝ 1/k²; SPHEREx-like”)
- Why missed: Reviewers focused on propagation, not the physics of the weights themselves.
- Problem: Calling w ∝ k² a “CMB Fisher” weight and w ∝ 1/k² an “LSS SDB Fisher” weight is, at best, schematic. The true Fisher kernels for a bispectrum amplitude template depend on survey mode counts, Cℓ or P(k) covariance, and triangle counting; they are not pure power laws of k. Using such toy weights can be fine for a toy exercise, but labeling them “Fisher” invites misinterpretation and makes the resulting r values appear survey‑optimal when they are not.
- Required fix: Either (i) rename these to “toy weights” and move the quantitative r results that rely on them to an explicit toy‑metric appendix, or (ii) provide the exact Fisher weights used (equations and normalizations) for the CMB and SPHEREx cases and recompute r accordingly.

P2-META-M4 — BF vs. SSFSR omits ns‑uncertainty marginalization (hidden conditioning)
- Severity: MAJOR
- Location: Sec. VI.C, Table III and surrounding text (pp. 12–16)
- Why missed: Other reports critiqued priors and σ, not the conditioning on ns.
- Problem: The SSFSR competitor is treated as a point model at fNL ≈ (5/12)(1−ns) ≈ 0.015 with no uncertainty. In reality, SSFSR’s gauge‑frame “prediction” should be marginalized over the measured uncertainty on ns (Planck), which broadens the competitor likelihood and reduces the BF advantage. Treating SSFSR as exact δ(fNL=0.015) is hidden conditioning that artificially boosts BF vs. SSFSR.
- Required fix: Include a Gaussian prior on fNL for SSFSR induced by the Planck posterior on ns (and any slow‑roll corrections), and recompute the BF vs. SSFSR column. Report both numbers (with/without ns marginalization) and use the marginalized one in any headline comparison.

P2-META-M5 — Contradictory statements on which triangle configurations dominate r
- Severity: MAJOR
- Location: Sec. III.B, p. 8 (paragraphs on squeezed cutoffs and log‑weighted grid) vs. earlier in same section (CMB‑Fisher upweights squeezed)
- Why missed: Prior reviews flagged lack of data behind the cutoff test but not the contradiction.
- Problem: The text first argues the signal‑only “CMB Fisher” weighting upweights squeezed configurations (hence r = 0.876). Two paragraphs later it asserts “the squeezed‑limit cutoff is completely insensitive … confirming that the overlap is dominated by the intermediate and folded triangle configurations.” These statements can both be true for different weightings, but as written they read as contradictory drivers of the same r headline without clear separation.
- Required fix: Separate the statements explicitly by weighting scheme: explain that (i) in the toy “CMB Fisher” metric squeezed shapes dominate, but (ii) in the LSS/SPHEREx‑like metric the mismatch is driven by folded/intermediate triangles, and quantify each with plots or tables.

P2-META-m1 — Ambiguous equality notation for folded configuration in Table I
- Severity: MINOR
- Location: Table I, p. 5, folded row “(k1=2k2=2k3)”
- Why missed: Others focused on legend/colour issues.
- Problem: “k1=2k2=2k3” is ambiguous; the intended folded limit is k2 = k3 = k and k1 = 2k (i.e., k1 = 2k2 and k1 = 2k3). As written it can be parsed as k1 = 2 k2 and also k2 = 2 k3.
- Required fix: Replace by “k2 = k3 = k, k1 = 2k” (and ensure the code used that ordering).

P2-META-m2 — Inconsistent use of “basis‑independent” vs. “measure‑independent”
- Severity: MINOR
- Location: Abstract p. 1 and Sec. II, multiple places
- Why missed: The term is used loosely; earlier reviews did not parse the semantics.
- Problem: The manuscript alternates between “basis‑independent” (coefficient‑space) and what is really “measure‑independent” (triangle‑space weighting). This can mislead readers into thinking the rcos distribution is invariant under null‑space sampling schemes.
- Required fix: Reserve “basis‑independent” for invariance of a fixed shape under reparameterization; use “metric‑independent” or specify the triangle‑space measure when discussing distributions over the null space.

P2-META-m3 — No estimator–observable mapping for the CFC/physical‑frame consistency‑relation aside
- Severity: MINOR
- Location: Abstract p. 1 and Conclusion p. 20
- Why missed: Others accepted the aside as context; no one asked for a mapping.
- Problem: The text repeatedly mentions that the CFC/physical‑frame local bispectrum tends to zero for SSFSR, contrasting with the gauge‑frame estimator used by SPHEREx. No quantitative mapping is provided between the two for the bounce or inflation, so the reader cannot assess whether any future “physical‑frame” reinterpretation would alter the survey‑frame discrimination.
- Required fix: Add one paragraph clarifying how, if at all, the bounce prediction transforms to the CFC frame at leading order, and why this does or does not affect the survey‑frame forecasts.

## Meta-review recommendation
MAJOR REVISIONS

The most serious, new issue is the algebraic inconsistency between Eqs. (1) and (2): as written, P cancels and BNL loses all dependence on the polynomial coefficients, invalidating the null‑space/mismatch program that underpins much of the paper. The injection–recovery “validation” also mixes 2D/3D channels in a way that is not methodologically acceptable for a 3D LSS forecast. Appendix A’s symmetry‑factor usage needs a concrete derivation, and several claims about “basis‑independence” and “Fisher weights” must be clarified or relabeled.

Given the union of all six reviews, I count 10–12 essential/major blockers (including algebraic, statistical, and presentation issues). My confidence that the paper would survive external (non–bigbounce) PRD peer review without a substantial rewrite is low at present; the central definitional inconsistency and methodological gaps would likely lead to rejection unless they are corrected with a full recalculation and a tighter, more transparent presentation.