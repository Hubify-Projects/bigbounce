# EXT11 Harvest — P2 — Gemini

- Provider: Gemini
- Model/Effort: 2.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/1ed5eac442bc1b16
- PDF md5: ab99c187 (paper2_fnl_forecast_v1.7.64_ab99c187.pdf)
- Harvested: 2026-06-13 16:57 PDT

---

## Headline Verdict: ACCEPT

The closures applied in this iteration have successfully elevated the manuscript to a highly rigorous, self-consistent, and transparent state. By explicitly distinguishing between on-sky observables and theoretical discriminators, and by meticulously mapping out the systematic degradation pathways, the paper stands as a textbook example of a clean sensitivity recast.

The internal math checks out beautifully across all sections (including the template mismatch recoveries, the multi-tracer degeneracy factors, and the closed-form Bayesian integrals). The scientific narrative is robust, and the structural limits of the assumptions are honestly bounded.

## Review of Specific Closures

**1. The Operator-Algebra Audit (Cai vs. Li Discrepancy)**
The text now handles the factor-of-two discrepancy between Cai et al. and Li et al. with excellent mathematical authority. Framing the difference as a strict operator-algebra identity (i⟨[ζ³,L]⟩ = −2 Im⟨ζ³L⟩) rather than an ambiguous convention choice provides a definitive resolution for the reader. Retaining the Li et al. branch purely as a single-time-ordering structural stress test provides a helpful "worst-case" bound without diluting the primary physical framework.

**2. Covariance vs. Field-Scaling Clarification**
Modifying the prose around Equation 7 to explicitly state that it serves as a "heuristic primordial-field scaling check" completely resolves the major risk of misinterpreting it as a rigorous galaxy-covariance derivation. Referencing the multi-tracer bispectrum expansion lineage (Seljak, McDonald, Karagiannis et al.) anchors the baseline sensitivity appropriately.

**3. Template-Mismatch Bookkeeping & Priors**
The abstract-to-text alignment regarding the Bayes factors is now perfectly synchronized. Clearly stating that the headline BF ≈ 9–14 applies the noise-weighted r ≈ 0.84 template-mismatch bookkeeping, while Table II preserves the idealized r→1 endpoints, removes any potential confusion for a skimming reader. The inclusion of the continuous marginalization checks over the prior-width hyperparameter (σ_theory) and the GR contamination scale (σ_GR) confirms that the discrete grid results are highly stable baseline summaries.

**4. Einstein-Cartan-Holst (ECH) Torsion Bounding**
The explicit restriction of the mechanism-independence claim to a scalar-only contracting phase — and the proactive warning that significant fermion populations would reactivate the Barbero-Immirzi parameter through the dim-6 four-fermion channel — adds a layer of theoretical honesty that protects the paper's core assertion.

## Open or Minor Items (Purely Informational)

**MegaMapper Systematics Extrapolation:** The paper remains completely transparent that the systematic budget applied to MegaMapper's z=2–5 range is an illustrative stress test rather than an independently calibrated high-z Fisher matrix. Given that MegaMapper is a proposed Stage-V facility without a finalized instrument design, this scoping choice is entirely appropriate for a recast paper.

**Channel Hierarchy:** Section IX.D accurately frames the scale-dependent bias (SDB) joint (f_NL, n_{f_NL}) Fisher matrix as a subordinate diagnostic cross-check. This prevents any false equivalence with the headline multi-tracer galaxy bispectrum forecast.

The paper is ready for production.
