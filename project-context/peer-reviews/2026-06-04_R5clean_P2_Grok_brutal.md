# P2 2026-06-04_R5clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 13.4s

---

**Referee Report: P2**

**Paper length**: 22 pages. The claimed contribution is a template-overlap recast of published SPHEREx forecasts plus a Bayesian prior-sensitivity exercise. This does not justify 22 pages; the recommended maximum is 12–14 pages after removal of redundant self-referential prose, repeated assumption lists, and deferred-companion language.

**P2-E1 (ESSENTIAL)** — Abstract (entire block)  
Problem: The abstract does not accurately summarize what the paper proves. It contains narrative ranges (“3–5σ”, “5.2–5.5σ”, “BF ∼ 10–17”), an explicit statement that a joint Fisher significance “is not quoted here in the abstract until that release lands,” and a full paragraph on convention reversal that halves every quoted significance. These are not proved results but conditional forecasts under unverified assumptions (a)–(f) and an unresolved normalization choice.  
Required fix: Replace the abstract with a single-paragraph statement limited to what is actually demonstrated: the template overlap r = 0.84 ± 0.02, the adoption of the Heinrich et al. (2024) σ(fNL) = 0.7 without re-derivation, and the explicit caveat that the quoted significances are convention-dependent and assumption-dependent.

**P2-E2 (ESSENTIAL)** — Abstract and §X (conclusion)  
Problem: The paper presents 5.2–5.5σ (optimistic) and 3–5σ (post-systematics) as headline numbers while simultaneously stating that adoption of the Li & Brandenberger normalization halves every figure. No justification is given for privileging the Cai convention in the abstract and conclusion when the operator-algebra argument in Appendix A is not an independent derivation.  
Required fix: Either (i) adopt one convention throughout and state the resulting single significance, or (ii) present both conventions as equally plausible and report the halved range as the primary result.

**P2-E3 (ESSENTIAL)** — §II C and §VI (assumptions and Bayes factors)  
Problem: The Bayes-factor claims (BF ∼ 10–17) are conditioned on six unverified assumptions, an ad-hoc σtheory = 1.0 “recommended” prior, and the absence of prolonged post-bounce inflation. The paper does not demonstrate that these assumptions hold at the required order; it only states that they are required. Presenting BF ranges as evidence therefore constitutes overclaim.  
Required fix: Remove all numerical Bayes-factor quotes from the abstract and conclusion or re-label them explicitly as “illustrative under the six assumptions listed in §II C, none of which are observationally verified at cubic order.”

**P2-M1 (MAJOR)** — Abstract and §IV  
Problem: The paper repeatedly states that it “quantif[ies] for the first time the template mismatch.” This is false; the overlap integral between a non-local shape and the local template is standard in the PNG literature. The numerical value r = 0.84 ± 0.02 is new for this specific shape, but the framing is inflated.  
Required fix: Delete every “first time” or “novel” claim.

**P2-M2 (MAJOR)** — §II B and §II C  
Problem: The polynomial is underdetermined (3 constraints, 6 coefficients) by construction of the authors’ symmetrized basis. The paper acknowledges this but still quotes a central r = 0.85 ± 0.13 as if it were a controlled uncertainty rather than an artifact of basis choice. The 10,000-sample null-space scan does not resolve the ambiguity; it merely maps it.  
Required fix: Either adopt Cai et al.’s original single-time-ordering representation (no underdetermination) or state explicitly that the quoted r uncertainty is basis-dependent and not a physical model uncertainty.

**P2-M3 (MAJOR)** — §IV and §IX  
Problem: The headline forecast is a sensitivity recast of Heinrich et al. (2024), not an independent Fisher matrix. The paper acknowledges this in one sentence but then presents 5.2–5.5σ as “the headline forecast of this paper.” This is misleading.  
Required fix: Retitle the work as a “recast and Bayesian interpretation” and remove language implying new forecast machinery.

**P2-M4 (MAJOR)** — §VI (Monte Carlo ensembles)  
Problem: Three ensembles of 10^5 realizations each are presented as validation, yet the statistical conclusions are stated to be driven by the analytic formula. The Monte Carlo exercise therefore adds no new information beyond convergence checks.  
Required fix: Remove the Monte Carlo section or reduce it to a one-sentence convergence statement.

**P2-m1 (MINOR)** — Throughout  
Problem: Repeated self-referential phrases (“see Sec. II C”, “as discussed in §VII”, “Table II row 5”) make the text read like an internal audit log rather than a journal article.  
Required fix: Reduce cross-references to the minimum required for logical flow.

**P2-n1 (NIT)** — Abstract  
Problem: The sentence “the specific numerical significance is not quoted here in the abstract until that release lands” is review-log prose that should never appear in a submitted manuscript.  
Required fix: Delete.

**P2-n2 (NIT)** — §II A  
Problem: The phrase “the basis is thus fixed by the Cai-physics-restricted vertex structure, not by purely abstract S3 symmetry” is repeated in slightly different wording three times in two pages.  
Required fix: Condense to one occurrence.

**Summary recommendation**  
MAJOR REVISIONS

The manuscript is a sensitivity recast of existing forecasts with an added Bayesian prior scan. Its central numerical claims are fragile to an unresolved normalization convention that halves the quoted significance, rest on six unverified theoretical assumptions, and are presented with inflated language (“first time,” “headline forecast,” “minimally parameterized”). The abstract is excessively long, contains internal audit language, and does not accurately represent what is proved. A substantially shortened and re-framed version limited to the template-overlap calculation and an explicit statement of all caveats could be acceptable; the current version is not.